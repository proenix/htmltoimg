import json
import tempfile
import asyncio

from werkzeug.wsgi import wrap_file
from werkzeug.wrappers import Request, Response
from base64 import b64decode
from os import remove as rmfile
from pyppeteer import launch

async def screenshot(input_file, output_file, options):
    browser = await launch(options={'args': ['--no-sandbox']})
    page = await browser.newPage()
    await page.goto(input_file)
    settings = {
        'path': output_file, 
        'type': options.get('format', 'png'), 
        'clip': {
            'x':0, 
            'y': 0, 
            'width': float(options.get('width', 1000)), 
            'height': float(options.get('height', 1000)),
        },
        'omitBackground': options.get('transparent', False),
        'quality': options.get('quality', 100),
    }
    print("Generating image using: " + str(settings))
    await page.screenshot(settings)
    await browser.close()

@Request.application
def application(request):
    if request.method != 'POST':
        return

    with tempfile.NamedTemporaryFile() as output_file:
        output_file.flush()
        request_is_json = request.content_type.endswith('json')

        if (request_is_json):
            payload = json.loads(request.data)
            # Iterate through base64 encoded html pages adding them to 
            source_files = list()
            for page_content_base64_encoded in payload['contents'] :
                page_html_file = tempfile.NamedTemporaryFile(suffix='.html', delete=False)
                page_html_file.write(b64decode(page_content_base64_encoded))
                page_html_file.flush()
                source_files.append(page_html_file)

            # Add Global Options
            options = payload.get('options', {})

            # Extract input file_name (ignore if more than one page)
            input_file = [n.name for n in source_files]
            input_file = 'file://' + input_file[0]

            # Execute the command using asyncio coroutine as synced
            try:
                loop = asyncio.get_event_loop()
                coroutine = screenshot(input_file, output_file.name, options)
                loop.run_until_complete(coroutine)
            except Exception as e:
                print(e)
            
            # Delete html files manually after execution
            for page_html_file in source_files:
                try:
                    page_html_file.close()
                    rmfile(page_html_file.name)
                finally:
                    pass
            
            # Return Response with image
            return Response(
                wrap_file(request.environ, open(output_file.name, 'rb')),
                mimetype='image',
            )
    
    return

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        '127.0.0.1', 5000, application, use_debugger=True, use_reloader=True
    )
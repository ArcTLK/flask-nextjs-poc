# Flask + React (NextJS) deployment POC

## Flask
This is the backend server that will serve the NextJS frontend.

### Setup
1. Install latest version of Python.
2. Create a virtual environment.
3. Run `pip install -r requirements.txt`

### Deployment
1. Run `python main.py`

## React (NextJS)
This is the frontend application.

### Setup
1. Install latest version of NodeJS.
2. Move to the react directory.
3. Run `npm install`

### Development
1. Run `npm run dev`

### Deployment
1. Run `npm run build`

### Considerations
Images or other static assets in the app will need the base path (sub path) prefixed to them.

For example,
`src="/globe.svg"` would need to be written as ``src={`${BASE_PATH}/globe.svg`}``

This BASE_PATH can be modified in the `config.ts` file.

### Special configurations (already done for you)
Edit the `next.config.ts` to have the following configuration:
```
const nextConfig: NextConfig = {
  /* config options here */
  output: 'export',
  cleanDistDir: true,
  distDir: '../public',
  basePath: '/frontend'
}
````

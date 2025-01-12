import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  output: 'export',
  cleanDistDir: true,
  distDir: '../public',
  basePath: '/frontend'
};

export default nextConfig;

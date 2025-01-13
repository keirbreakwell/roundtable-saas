/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  distDir: 'build',
  images: {
    unoptimized: true,
  },
  experimental: {
    optimizeCss: true,    // CSS optimization
    forceSwcTransforms: true,  // Force faster transforms
  },
};

module.exports = nextConfig;
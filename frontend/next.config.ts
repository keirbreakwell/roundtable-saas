/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  distDir: 'build',
  images: {
    unoptimized: true,
  },
  experimental: {
    turbotrace: true,  // Added this for build caching
  },
};

module.exports = nextConfig;
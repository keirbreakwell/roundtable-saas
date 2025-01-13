/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  distDir: 'build', // Changed from 'out' to 'build'
  images: {
    unoptimized: true,
  },
};

module.exports = nextConfig;
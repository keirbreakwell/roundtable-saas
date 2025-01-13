/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  distDir: 'out', // Explicitly set output directory
  images: {
    unoptimized: true,
  },
};

module.exports = nextConfig;
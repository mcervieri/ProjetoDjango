/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./fitapp/**/*.html",
    "./fitapp/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#16a34a", // verde FitApp
          dark: "#15803d",
          light: "#22c55e",
        },
        darkbg: "#0f172a",
      },
      fontFamily: {
        sans: ["Poppins", "sans-serif"],
      },
    },
  },
  plugins: [],
};

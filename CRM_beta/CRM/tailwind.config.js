/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'client_app/templates/client_app/*.html',
    'core_app/templates/core_app/*.html',
    'dashboard/templates/dashboard/*.html',
    'lead/templates/lead/*.html',
    'team/templates/team/*.html',
    'userprofile/templates/userprofile/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

module.exports = function (grunt) {
  grunt.initConfig({
    sass: {
      dist: {
        options: {
          style: "compressed",
        },
        files: {
          "static/styles/main.css": "static/styles/main.scss",
        },
      },
    },
    watch: {
      sass: {
        files: ["static/styles/*.scss"],
        tasks: ["sass:dist"],
      },
    },
  });

  grunt.loadNpmTasks("grunt-contrib-sass");
  grunt.loadNpmTasks("grunt-contrib-watch");

  grunt.registerTask("default", ["sass:dist"]);
};

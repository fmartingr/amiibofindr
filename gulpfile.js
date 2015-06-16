var gulp = require('gulp'),
    watch = require('gulp-watch'),
    less = require('gulp-less'),
    livereload = require('gulp-livereload');

gulp.task('less', function() {
  gulp.src('amiibofindr/static/less/**/*.less')
    .pipe(less())
    .pipe(gulp.dest('amiibofindr/static/css'))
    .pipe(livereload());
});

gulp.task('watch', function() {
  livereload.listen({ start: true });
  gulp.watch('amiibofindr/**/less/**/*.less', ['less']);
});
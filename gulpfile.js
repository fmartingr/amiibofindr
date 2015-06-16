var gulp = require('gulp'),
    watch = require('gulp-watch'),
    less = require('gulp-less'),
    livereload = require('gulp-livereload'),
    concat = require('gulp-concat');

gulp.task('scripts', function() {
  return gulp.src([
      'bower_components/jquery/dist/jquery.js',
      'bower_components/uikit/js/uikit.js'
    ])
    .pipe(concat('app.js'))
    .pipe(gulp.dest('amiibofindr/static/dist'));
});

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

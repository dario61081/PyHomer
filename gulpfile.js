let gulp = require('gulp');
let sass = require('gulp-sass');

// Copy dependencies
gulp.task("compile", () => {
     return gulp.src('static/**/*.sass').pipe(sass({outputStyle: 'compressed'})).pipe(gulp.dest('static'));
});

gulp.task("default", gulp.serfies("compile"));
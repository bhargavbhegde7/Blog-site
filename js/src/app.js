var app = angular.module("myApp", ["ngRoute"]);
app.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "views/home.html"
    })
    .when("/contact", {
        templateUrl : "views/contact.html"
    })
    .when("/projects", {
        templateUrl : "views/projects.html"
    })
    .when("/cv", {
        templateUrl : "views/resume_bhargava_b_hegde.pdf"
    });
});

var myApp = angular.module('Task', ["ngStorage", "ngRoute", "ToDoListModule"]);

myApp.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
}]);



myApp.controller('MainController', ['$scope', '$http', '$sessionStorage', '$window', function ($scope, $http, $sessionStorage, $window) {

    $scope.init = function () {

    }

}]);
var myApp = angular.module('Login', ["ngStorage"]);

myApp.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
}]);


myApp.controller('LoginController', ['$scope', '$http', '$window', function ($scope, $http, $window) {

    $scope.login = async function () {
        let params = {
            "username": $scope.username,
            "password": $scope.password
        }
        let response = await $http.post("/token/", params).success(function (response) {
            window.localStorage.setItem("token", response["token"]);
            $window.location.href = '/home/';
        }).error(function (data, status) {
            console.log(data);
        }).finally(function () {
            $scope.mostrar = false;
        });

    }

}]);
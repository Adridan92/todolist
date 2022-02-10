var myApp = angular.module('ToDoListModule', []);


myApp.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/', {
            template: '<task-list></task-list>'
        })
        .otherwise({
            redirectTo: '/'
        });
}]);


myApp.controller('ToDoListController', ['$scope', function ($scope) {


}]);
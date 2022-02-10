var myapp = angular.module('ToDoListModule');

myapp.factory('taskService', ['$http', '$q', '$localStorage', function ($http, $q, $localStorage) {

    var allTasks = null;

    async function getTasks() {
        let deferred = $q.defer();
        let token = window.localStorage.getItem("token");
        let headerOptions = {
            "Authorization": "Token " + token,
            "Content-Type": "application/json"
        }

        if (allTasks == null) {
            await $http.get('/tasks/', {
                headers: headerOptions
            }).success(function (data) {
                deferred.resolve(data);
            }).error(function (data, status) {
                deferred.reject();
            })
            allTasks = deferred.promise;
        }


        return allTasks;
    }


    async function insertTask(params) {
        let deferred = $q.defer();
        let token = window.localStorage.getItem("token");
        let headerOptions = {
            "Authorization": "Token " + token,
            "Content-Type": "application/json"
        }

        await $http.post('/tasks/', params, {
            headers: headerOptions
        }).success(function (data) {
            deferred.resolve(data);
        }).error(function (data, status) {
            deferred.reject();
        })
        return deferred.promise;

    }

    async function deleteTask(params) {
        let deferred = $q.defer();
        let token = window.localStorage.getItem("token");
        let headerOptions = {
            "Authorization": "Token " + token,
            "Content-Type": "application/json"
        }
        await $http.delete('/tasks/' + params["id"] + "/", {
            headers: headerOptions
        }).success(function (data) {
            deferred.resolve(data);
        }).error(function (data, status) {
            deferred.reject();
        })

        allTasks = null;

        return getTasks();
    }


    async function updateTask(params) {
        let deferred = $q.defer();
        let token = window.localStorage.getItem("token");
        let headerOptions = {
            "Authorization": "Token " + token,
            "Content-Type": "application/json"
        }
        await $http.put('/tasks/' + params["id"] + "/", params, {
            headers: headerOptions
        }).success(function (data) {
            deferred.resolve(data);
        }).error(function (data, status) {
            deferred.reject();
        })

        allTasks = null;

        return getTasks();
    }




    return {
        getTasks: getTasks,
        insertTask: insertTask,
        deleteTask: deleteTask,
        updateTask: updateTask,
    }


}]);


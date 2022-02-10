angular.module('ToDoListModule').component('taskList', {
    templateUrl: '/static/app/modules/todolist/components/task/task.template.html',
    controller: [
        'taskService', '$scope',
        function (taskService, $scope,) {
            var ctrl = this;

            $scope.editing = false;
            $scope.taskList = [];
            $scope.currentId = -1;
            $scope.allStatus = [{ "id": 1, "name": "pendiente" }, { "id": 2, "name": "En proceso" }, { "id": 3, "name": "Terminado" }];

            ctrl.$onInit = async function () {
                await taskService.getTasks().then(function (data) {
                    $scope.taskList = data;
                    $scope.$digest();
                });
            }

            ctrl.selectTask = async function (id) {
                let aux = $scope.taskList.filter(item => item.id == id);
                let item = aux[0];
                let aux2 = $scope.allStatus.filter(item2 => item2.id == item.status);
                $scope.title = item.title;
                $scope.description = item.description;
                $scope.status = aux2[0];
                $scope.editing = true;
                $scope.currentId = id;
            }

            ctrl.cancel = async function () {
                ctrl.clear();
                $scope.editing = false;
                $scope.$digest();
            }

            ctrl.clear = async function () {
                $scope.title = "";
                $scope.description = "";
                $scope.status = "";
                $scope.currentId = -1;
                $scope.$digest();
            }



            ctrl.insert = async function () {
                let params = {
                    "title": $scope.title,
                    "description": $scope.description,
                    "status": $scope.status.id
                }

                await taskService.insertTask(params).then(function (data) {
                    $scope.taskList.push(data);
                    ctrl.clear();
                    $scope.$digest();
                });

            }

            ctrl.delete = async function (id) {
                let params = {
                    "id": id
                }
                await taskService.deleteTask(params).then(function (data) {
                    $scope.taskList = data;
                    $scope.$digest();
                });
            }

            ctrl.update = async function (id) {
                let params = {
                    "id": $scope.currentId,
                    "title": $scope.title,
                    "description": $scope.description,
                    "status": $scope.status.id
                }

                await taskService.updateTask(params).then(function (data) {
                    $scope.taskList = data;
                    ctrl.clear();
                    $scope.$digest();
                });

            }




        },
    ],
});

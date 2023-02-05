export class Department{

    listOfDepartment:string[];

    constructor(objectModel:any){
        this.listOfDepartment = objectModel['departments'];
    }

    getDepartment(){
        return this.listOfDepartment;
    }
}
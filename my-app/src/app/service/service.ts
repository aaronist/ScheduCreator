import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Department } from '../data/department';

@Injectable({
    providedIn: 'root'
})

export class service{
    expressBaseUrl:string = 'http://localhost:5000';

    constructor(private http:HttpClient){

    }

    private sendRequestToServerGet(endpoint:string):Promise<any>{
        let temp = this.http.get(this.expressBaseUrl+endpoint).toPromise();
        return Promise.resolve(temp);
    }

    private sendRequestToServerPost(endpoint:string):Promise<any>{
        let temp = this.http.get(this.expressBaseUrl+endpoint).toPromise();
        return Promise.resolve(temp);
    }

    private sendRequestToServerPut(endpoint:string):Promise<any>{
        let temp = this.http.get(this.expressBaseUrl+endpoint).toPromise();
        return Promise.resolve(temp);
    }

    getDepartment(endpoint:string){

        return this.sendRequestToServerGet(endpoint).then((data) =>{
    
            return data;
        });
    }

    getCourseNumber(endpoint:string){
        
    }


}
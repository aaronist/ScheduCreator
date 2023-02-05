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

    private sendRequestToServerPost(endpoint:string,body:any):Promise<any>{
        const httpOptions = {
            headers: new HttpHeaders({
<<<<<<< HEAD
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, POST, ...'
=======
           
                'Content-Type': 'application/json'
>>>>>>> ba14c2455bfc2cd905cf207ad5f30d1eb2dfd61f
            })
        };
        let temp = this.http.post(this.expressBaseUrl+endpoint,body,httpOptions).toPromise();
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

    getCourseNumber(endpoint:string,term1:string,department1:string){
        const data = {
            term: term1,
            department: department1
        }
        this.sendRequestToServerPost(endpoint,data);
    }

    getCourse(endpoint:string){
        return this.sendRequestToServerGet(endpoint).then((data) =>{

            return data;
        })
    }

    getSchedule(endpoint:string){
        return this.sendRequestToServerGet(endpoint).then((data)=>{
            return data;
        })
    }

    


}
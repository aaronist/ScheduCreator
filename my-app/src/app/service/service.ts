import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})

export class service{
    expressBaseUrl:string = 'http://localhost:5000';

    constructor(private http:HttpClient){
        this.http.get('http://localhost:5000').subscribe(data => {
            console.log(data);
          });
    }

    private sendRequestToExpress(endpoint:string):Promise<any>{
        let temp = this.http.get(this.expressBaseUrl+endpoint).toPromise();
        return Promise.resolve(temp);
    }

    test(){
        console.log("testing");
        
    }
}
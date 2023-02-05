import { Component, NgModule } from '@angular/core';
import { service } from 'src/app/service/service';
import { FormsModule } from '@angular/forms';


@Component({
  selector: 'app-schedule',
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.css'],
  providers: [service]
})
export class ScheduleComponent {
  departments: any;
  searchDepartment:string = "";
  terms;
  searchTerm:string = "";
  courseNumbers: any;
  searchCourse:string = "";
  
  schedule:any;
  
  constructor(private service:service){

    this.terms = ['Winter 2022', 'Spring 2022', 'Fall 2022', 'Winter 2023'];

    this.service.getDepartment("/department").then((data) =>{
      this.departments = data;

      console.log(this.departments);
    });

    //this.service.getCourseNumber("/courseNumber");
    
  }

  assignTerm(){
    console.log("term is " + this.searchTerm);

  }

  getCourse(){

    console.log("term is " + this.searchDepartment);
    this.service.getCourseNumber("/course",this.searchTerm,this.searchDepartment);
    this.get();
  }

  get(){

    this.service.getCourse("/courseList").then((data)=>{

      this.courseNumbers = data;

      console.log("coursenumbers are " + this.courseNumbers);
    })
  }

  getSchedule(){
    console.log("come one");
    this.service.getSchedule("/schedule").then((data)=>{

        console.log(data);
        this.schedule = data;
    })
  }



  
}


import { Component } from '@angular/core';
import { service } from 'src/app/service/service';
import { Department } from 'src/app/data/department';

@Component({
  selector: 'app-schedule',
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.css'],
  providers: [service]
})
export class ScheduleComponent {
  department: any;
  terms;
  courseNumbers: any;
  
  constructor(private service:service){

    this.terms = ['Winter 2022', 'Spring 2022', 'Fall 2022', 'Winter 2023'];

    this.service.getDepartment("/department").then((data) =>{
      this.department = data;

      console.log(this.department);
    });

    this.service.getCourseNumber("/courseNumber");

    this.courseNumbers = ['ICS31'];
    
    
  }

  
}

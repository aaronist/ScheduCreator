import { Component } from '@angular/core';
import { service } from 'src/app/service/service';
@Component({
  selector: 'app-schedule',
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.css'],
  providers: [service]
})
export class ScheduleComponent {
  terms;
  departments;
  courseNumbers;
  
  constructor(private service:service){

    this.terms = ['Winter 2022', 'Spring 2022', 'Fall 2022', 'Winter 2023'];

    this.courseNumbers = ['ICS31'];

    this.departments = this.service.getInitialData();

    console.log(this.departments)
    
  }

  
}

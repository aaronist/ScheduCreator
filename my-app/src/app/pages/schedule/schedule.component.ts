import { Component } from '@angular/core';

@Component({
  selector: 'app-schedule',
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.css']
})
export class ScheduleComponent {
  terms;
  departments;
  courseNumbers;

  constructor(){
    this.terms = ['Spring:2023'];
    this.departments = ['ICS'];
    this.courseNumbers = ['ICS31'];

  }

  
}

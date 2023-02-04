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

    this.terms = ['Spring:2023'];
    this.departments = ['ICS'];
    this.courseNumbers = ['ICS31'];

    this.service.test();

  }

  
}

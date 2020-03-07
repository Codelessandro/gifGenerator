import { Component } from '@angular/core';
import mockdata from "../data/mockdata";



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'gifGenerator';
  data:any = []

  constructor() {
  }

  showExample() {
    this.data=mockdata
  }


}

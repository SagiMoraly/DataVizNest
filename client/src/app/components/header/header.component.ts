import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
})
export class HeaderComponent implements OnInit {
  title: string = 'angular-python-project';

  ngOnInit(): void {}

  toggleAddTask() {
    console.log('toggle');
  }
}

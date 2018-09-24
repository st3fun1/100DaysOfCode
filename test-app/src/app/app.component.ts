import { Component } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/operators/map';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'test-app';
  constructor(
    private http: Http
  ) {}

  ngOnInit() {
    this.http.get('/some-route').pipe(
      response => response
    ).subscribe( (data) => console.log(data));
  }
}

import { Component, OnDestroy, OnInit } from "@angular/core";
import { interval, Observable, Subscription } from "rxjs";
import { map, filter } from "rxjs/operators";

@Component({
  selector: "app-home",
  templateUrl: "./home.component.html",
  styleUrls: ["./home.component.css"],
})
export class HomeComponent implements OnInit, OnDestroy {
  private firstObsSubscription: Subscription;

  constructor() {}

  ngOnInit() {
    /* this.firstObsSubscription = interval(1000).subscribe(count => {
      console.log(count);
    }); */
    // Custom Observable
    const customIntervalObservable = Observable.create((observer) => {
      let count = 0;
      setInterval(() => {
        observer.next(count);
        if (count === 5) {
          observer.complete();
        }
        if (count > 3) {
          observer.error(new Error("Count is greater than 3!!"));
        }
        count++;
      }, 1000);
    });

    /* this.firstObsSubscription = customIntervalObservable.subscribe(
      (count) => {
        console.log(count);
      },
      (error) => {
        console.log(error);
        alert(error.message);
      },() => {
        console.log('Completed');
      }
    ); */
    // Using operators
    this.firstObsSubscription = customIntervalObservable.pipe(filter((data)=> {
      return data >0;
    }),map(data => {
      return 'Record ' + data;
    })).subscribe(
      (count) => {
        console.log(count);
      },
      (error) => {
        console.log(error);
        alert(error.message);
      },() => {
        console.log('Completed');
      }
    );
  }

  ngOnDestroy() {
    this.firstObsSubscription.unsubscribe();
  }
}

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { DashboardComponent } from './dashboard.component';
import { PaymentPageComponent } from './payment-page/payment-page.component';
import { ReportsPageComponent } from './reports-page/reports-page.component';
import { UserPaymentPageComponent } from './user-payment-page/user-payment-page.component';

@NgModule({
    declarations: [
        PaymentPageComponent,
        ReportsPageComponent,
        UserPaymentPageComponent
    ],
    imports: [
      CommonModule,
    ],
    exports: []
  })
  export class DashboardModule { }

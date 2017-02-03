//#include <cmath>
#include <math.h>
#include <iostream>
#include <string.h>
//#include "TMatrixT.h"
//#include "TMatrixTBase.h"
//#include "TFile.h"
//#include "interface/CMSStyle.C" 
//#include "TString.h"
//#include "TH1.h"
//#include "TH1F.h"
//#include "TH2.h"
//#include <map>
//#include "params_arg_Hmx.h"
//#include "TMath.h"
//#include "interface/utilities.h"
//#include "TRandom3.h"

using namespace std;

void Stop();
double Ln_of_Gamma(double xx);
double factorial(int n);
double Ln_of_Factorial(int n);
double nCr(int n, int k);
double beta(double z, double w);
void incomplete_gamma_func_P_by_series_representation(double *gamser, double a, double x, double *gln);
void incomplete_gamma_func_Q_by_continuous_fractions(double *gammcf, double a, double x, double *gln);
double incomplete_gamma_func_P(double a, double x) ;
double incomplete_gamma_func_Q(double a, double x) ;
double  Chi_squared_CDF(double x, double k);
double Poisson_CDF(double x, double l);
double erff_(double x);
double erffc(double x);

//CDF calculators
//double PoissonCDF(double poissMean, double poissSTDev, int nObs, int nDice); 
//meant to tell you what probability the poisson dist comes out >= nObs. 
//the estimate of the poisson mean (poissmean) has gaussian uncertinty poisssSTDev


/*
Regularized gamma function P = g/G
Chi2 CDF = P(k/2,x/2)
g =  lower incomplete Gamma function 
G =  Gamma function G(N)
	if N is a postitive integer, G(N) = (N-1)!


*/
void Stop(){
    std::terminate;
}

double Ln_of_Gamma(double xx){
	//returns the value of ln( Gamma(xx) ) for xx > 0
	//Taken from Numerical Recipes in C page 214
	//internal arithamtic will be done in double precision. 
	//gammln
	double x,y,tmp,ser;
	static double cof[6]={76.18009172947146,-86.50532032941677,
		24.01409824083091,-1.231739572450155,
		0.1208650973866179e-2,-0.5395239384953e-5};
	int j;
	y=x=xx;
	tmp=x+5.5;
	tmp -= (x+0.5)*log(tmp);
	ser=1.000000000190015;
	for (j=0;j<=5;j++) ser += cof[j]/++y;
	return -tmp+log(2.5066282746310005*ser/x);
}

//if N is a positive integer, Gamma(N) = (N-1)!

double factorial(int n){
	//returns the value of n! as a floating point number, it's exact up to 
	static int ntop=4;
	static double a[33]={1.0,1.0,2.0,6.0,24.0}; //Fill in table only as required.
	int j;
	if (n < 0){
		cout<<"Error! Negative input to factorial"<<endl;
		Stop();
	}
	if (n > 32) return exp(Ln_of_Gamma(n+1.0)); //effectively sterling approxomation. 
	//Larger value than size of table is required. Actually, this big a value is going to overflow
	//on many computers, but no harm in trying.
	while (ntop<n) { //Fill in table up to desired value.
		j=ntop++;
		a[ntop]=a[j]*ntop;
	}
	return a[n];
}

double Ln_of_Factorial(int n) {
	//Returns ln(n!).
	//double Ln_of_Gamma(double xx);
	static double a[101]; //A static array is automatically initialized to zero.
	if (n < 0){
		cout<<"Error! Negative input to factorial"<<endl; 
		Stop();
	}
	if (n <= 1) return 0.0;
	if (n <= 100) return a[n] ? a[n] : (a[n]=Ln_of_Gamma(n+1.0)); //In range of table.
	else return Ln_of_Gamma(n+1.0); //Out of range of table.
}

double nCr(int n, int k){
//Returns the binomial coefficient n nCr k as a floating-point number.
//double factln(int n);
	return floor(0.5+exp(Ln_of_Factorial(n)-Ln_of_Factorial(k)-Ln_of_Factorial(n-k)));
//The floor function cleans up roundoff error for smaller values of n and k.
}
//if you need a lot of binomial coificients, its best to use the recursion/recurrence relations in 6.1.7 of Numerical Recipes in C, page 215.

double beta(double z, double w){
//Returns the value of the beta function B(z, w).
	return exp(Ln_of_Gamma(z)+Ln_of_Gamma(w)-Ln_of_Gamma(z+w));
}

/*
Incomplete Gamma Function P(a,x)
 = gamma(a,x)/Gamma(a)
Q(a,x) = 1-P(a,x) //also called the incomplete gamma function 
Gamma(a,x) = Gamma(a) - gamma(a,x) //the upper incomplete gamma function. 
gamma(a,x) // the lower incomplete gamma function
*/


#define ITMAX 100 //Maximum allowed number of iterations.
void incomplete_gamma_func_P_by_series_representation(double *gamser, double a, double x, double *gln){
	//Returns the incomplete gamma function P(a, x) evaluated by its series representation as gamser.
	//gser
	//Also returns ln Γ(a) as gln.
	//double Ln_of_Gamma(double xx);
	//void nrerror(char error_text[]);
	int n;
	double sum,del,ap;
	*gln=Ln_of_Gamma(a);
	if (x <= 0.0) {
		if (x < 0.0) cout<<"Error: x less than 0 in routine incomplete_gamma_func_P_by_series_representation"<<endl;
		*gamser=0.0;
		return;
	} else {
		ap=a;
		del=sum=1.0/a;
		for (n=1;n<=ITMAX;n++) {//100 = max itterations
			++ap;
			del *= x/ap;
			sum += del;
			if (fabs(del) < fabs(sum)*3.0e-7) {
				*gamser=sum*exp(-x+a*log(x)-(*gln));
				return;
			}
		}
		cout <<"Error: a too large, max itteration too small in routine incomplete_gamma_func_P_by_series_representation"<<endl;
		return;
	}
}

#define FPMIN 1.0e-300 //Number near the smallest representable floating-point number.
void incomplete_gamma_func_Q_by_continuous_fractions(double *gammcf, double a, double x, double *gln) {
//	Returns the incomplete gamma function Q(a, x) evaluated by its continued fraction representation as gammcf. Also returns ln Γ(a) as gln.
	int i;
	double an,b,c,d,del,h;
	*gln=Ln_of_Gamma(a);
	b=x+1.0-a; //Set up for evaluating continued fraction
		//by modified Lentz’s method (section 5.2) with b0 = 0.
		c=1.0/FPMIN;
	d=1.0/b;
	h=d;
	for (i=1;i<=ITMAX;i++) { //Iterate to convergence.
		an = -i*(i-a);
		b += 2.0;
		d=an*d+b;
		if (fabs(d) < FPMIN) d=FPMIN;
		c=b+an/c;
		if (fabs(c) < FPMIN) c=FPMIN;
		d=1.0/d;
		del=d*c;
		h *= del;
		if (fabs(del-1.0) < 3.0e-7) break; //3e-7 is the relative accuracy. 
	}
	if (i > ITMAX) cout<<"Error: a too large, max iterations too small in incomplete_gamma_func_Q_by_continuous_fractions"<<endl;
	*gammcf=exp(-x+a*log(x)-(*gln))*h;// Put factors in front.
}

double incomplete_gamma_func_P(double a, double x) {
	//Returns the incomplete gamma function P(a, x).
	double gamser,gammcf,gln;
	if (x < 0.0 || a <= 0.0){
		cout<<"Invalid arguments in routine gammp"<<endl; 
		Stop();
	}
	if (x < (a+1.0)) { //Use the series representation.
		incomplete_gamma_func_P_by_series_representation(&gamser,a,x,&gln);
		return gamser;
	} else { //Use the continued fraction representation
		incomplete_gamma_func_Q_by_continuous_fractions(&gammcf,a,x,&gln);
		return 1.0-gammcf; //and take its complement.
	}
}

double incomplete_gamma_func_Q(double a, double x) {
	//Returns the incomplete gamma function Q(a, x) ≡ 1 − P(a, x).
	double gamser,gammcf,gln;
	if (x < 0.0 || a <= 0.0){
		cout<<"Invalid arguments in routine gammq"<<endl; 
		Stop();
	}
	if (x < (a+1.0)) { //Use the series representation
		incomplete_gamma_func_P_by_series_representation(&gamser,a,x,&gln);
		return 1.0-gamser; //and take its complement.
	} else { //Use the continued fraction representation.
		incomplete_gamma_func_Q_by_continuous_fractions(&gammcf,a,x,&gln);
		return gammcf;
	}
}

double Chi_squared_CDF(double x, double k){
	//p(X>x) for a chi2 distribution of k DOF. 
	return incomplete_gamma_func_P(k/2.0, x/2.0);
}

double Poisson_CDF(double x, double l){
	//returns the probability of a poisson outcome in [0,x) = [0,x-1] = <x, for a poisson distiibution with parameter l, 
	if(x==0) return exp(-l);
	return incomplete_gamma_func_Q(x,l);
}

double erff_(double x) {
	//Returns the error function erf(x).
	return x < 0.0 ? -incomplete_gamma_func_P(0.5,x*x) : incomplete_gamma_func_P(0.5,x*x);
}

double erffc(double x) {
	//Returns the complementary error function erfc(x).
	return x < 0.0 ? 1.0+incomplete_gamma_func_P(0.5,x*x) : incomplete_gamma_func_Q(0.5,x*x);
}


/*double erfc(double x){
//Returns the complementary error function erfc(x) with fractional error everywhere less than 1.2 × 10−7.
	double t,z,ans;
	z=fabs(x);
	t=1.0/(1.0+0.5*z);
	ans=t*exp(-z*z-1.26551223+t*(1.00002368+t*(0.37409196+t*(0.09678418+
						t*(-0.18628806+t*(0.27886807+t*(-1.13520398+t*(1.48851587+
										t*(-0.82215223+t*0.17087277)))))))));
	return x >= 0.0 ? ans : 2.0-ans;
}
double erf(double x){
	return 1.0 - erfc(x);
}*/

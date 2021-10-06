#include <iostream>                              
#include <fstream>                              
#include <cstdlib>   // exit
#include <cmath>

using namespace std;

static const int S_MAX = 80;
static const int s_min = 20;

int main( int argc, char* argv[] )
{
	int i = 0;
	int inventory = S_MAX;
	int d_i, o_i_minus_1;
	double mu_sum = 0;      /* setup */
	double l_plus_sum = 0;  /* holding */
	double l_minus_sum = 0; /* shortage */
	double order_sum = 0;   /* mu */
	double demand_sum = 0;

	ifstream data( argc > 1 ? argv[1] : "/dev/null" );
	if( !data ) {
		cerr << "Error opening data file." << endl;
		::exit(1);
	}

  	while( data >> d_i ) {

		++i;

		/***
		 * Not considered on first pass through loop due to 
		 * inventory initial value
		 *
		 * technically this is inventory is l_{i-1}
		 */
		if( inventory < s_min ) {
			/* order! */
			o_i_minus_1 = S_MAX - inventory;
			mu_sum++;
			order_sum += o_i_minus_1;
			/* speedy delivery to you */
			inventory += o_i_minus_1;
		} 

		demand_sum += d_i;

		if( inventory > d_i ) {
			/* plenty of cars (area of trapezoid) */
			l_plus_sum += (inventory - d_i/2.0);
		} else {
			/* back-ordering (areas of similar triangles */
			l_plus_sum += pow(inventory,2) / (2*d_i);
			l_minus_sum += pow(d_i-inventory,2) / (2*d_i);
		}

		/* l_i inventory */
		inventory -= d_i;
	}


	/***
	 * flow balanced system!
	 */
	if( inventory < S_MAX ) {
		order_sum += S_MAX - inventory;
		mu_sum++;
	}

	if( i ) {
		cout << i << " intervals S=" << S_MAX << " s=" << s_min << endl;
		cout << "average demand    " << (demand_sum/i) << endl;
		cout << "average order     " << (order_sum/i) << endl;
		cout << "setup frequency   " << (mu_sum/i) << endl;
		cout << "average holding   " << (l_plus_sum/i) << endl;
		cout << "average shortage  " << (l_minus_sum/i) << endl;
	}

	data.clear();
	data.close();
	return 0;
}


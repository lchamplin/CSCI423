import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class codingsis {
	public static final int S_MAX = 80;
	public static final int s_min = 20;
	public static void main ( String args[] )
	{
		int i = 0;
		int inventory = S_MAX;
		int d_i, o_i_minus_1;
		double mu_sum = 0;      /* setup */
		double l_plus_sum = 0;  /* holding */
		double l_minus_sum = 0; /* shortage */
		double order_sum = 0;   /* mu */
		double demand_sum = 0;

		try( Scanner data = new Scanner( new File( args.length > 0 ? args[0] : "/dev/null" ))  ) {
			while( data.hasNext() ) {
				++i;

				/**
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

				d_i = data.nextInt();
				demand_sum += d_i;

				if( inventory > d_i ) {
					/* plenty of cars (area of trapezoid) */
					l_plus_sum += (inventory - d_i/2.0);
				} else {
					/* back-ordering (areas of similar triangles */
					l_plus_sum += Math.pow(inventory,2) / (2*d_i);
					l_minus_sum += Math.pow(d_i-inventory,2) / (2*d_i);
				}

				/* l_i inventory */
				inventory -= d_i;

			}
			data.close();

			/**
			 * flow balanced system!
			 */
			if( inventory < S_MAX ) {
				order_sum += S_MAX - inventory;
				mu_sum++;
			}

			if( i > 0 ) {
				System.out.format( "%d intervals S=%d s=%d\n", i, S_MAX, s_min );
				System.out.format( "average demand    %f\n", (demand_sum/i) );
				System.out.format( "average order     %f\n", (order_sum/i) );
				System.out.format( "setup frequency   %f\n", (mu_sum/i) );
				System.out.format( "average holding   %f\n", (l_plus_sum/i) );
				System.out.format( "average shortage  %f\n", (l_minus_sum/i) );
			}

			System.exit(0);
		} catch ( FileNotFoundException e ) {
			System.err.println( "Error opening data file." );
		} catch ( Exception e ) {
			System.err.println( e.getClass() );
		}
		System.exit(1);

	}
}


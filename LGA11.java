import java.io.Console;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.Random;

public class LGA11 {

        public enum Type{
                ARRIVAL, FEEDBACK, JOBCOMPLETE
        }

        public static class Event implements Comparable<Event>
        {
                public double at;
                public Type type;
                public double service;

                Event(double a, Type t, double s){
                        this.at = a;
                        this.type = t;
                        this.service = s;
                }

                @Override
                public int compareTo(Event e){
                        return (int)(this.at - e.at);
                }
        };

	public static void main ( String args[] )
	{
		List<Event> eventList = new ArrayList<>();
                eventList.clear();
                double t = 0.0; //simulation clock
                double tau = 1000.0; //no new events after time tau
                Queue<Event> jobQueue = new ArrayDeque<>();
                jobQueue.clear();
                boolean inService = false;
                int newJobCount = 0;
                int jobsServiced = 0;

                Random rand = new Random();

                double at = Math.log(1 - rand.nextDouble())/(-2.0);
                double service = rand.nextDouble();
                Event firstArrival = new Event(at, Type.ARRIVAL, service);
                eventList.add(firstArrival);
                System.out.println(firstArrival.at);
                System.out.println(firstArrival.type);
                System.out.println(firstArrival.service);

                while(eventList.size() > 0){
                        Collections.sort(eventList);
                        Event event = eventList.remove(0);
                        t = event.at;
                        // System.out.println(t);

                        if(event.type == Type.ARRIVAL || event.type == Type.FEEDBACK){
                                Event nextArrival = new Event(0.0, null, 0.0);
                                if(event.type == Type.ARRIVAL){
                                        // System.out.println("arrival");
                                        newJobCount++;
                                        nextArrival.at = t + Math.log(1 - rand.nextDouble())/(-2.0);
                                        if(nextArrival.at < tau){
                                                nextArrival.type = Type.ARRIVAL;
                                                nextArrival.service = rand.nextDouble();
                                                eventList.add(nextArrival);
                                        }

                                }
                                jobQueue.add(event);
                        }
                        else if(event.type == Type.JOBCOMPLETE){
                                // System.out.println("complete");
                                if(rand.nextDouble() < 0.25){
                                        Event feedbackArrival = new Event(0.0, null, 0.0);
                                        feedbackArrival.at = t + Math.log(1 - rand.nextDouble())/(-1.0);
                                        feedbackArrival.type = Type.FEEDBACK;
                                        feedbackArrival.service = event.service/2.0;
                                        eventList.add(feedbackArrival);
                                }
                                inService = false;
                        }
                        if(!inService && jobQueue.size() > 0){
                                // System.out.println("not in service");
                                event = jobQueue.remove();
                                event.at = t + event.service;
                                event.type = Type.JOBCOMPLETE;
                                eventList.add(event);
                                inService = true;
                                jobsServiced++;
                        }

                }
                System.out.println("t:"+t);
                System.out.println("newJobCount:"+newJobCount);
                System.out.println("jobsServiced:"+jobsServiced);
	}
}




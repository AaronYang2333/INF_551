import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class count {

    private static String MAX_VALUE = "MAX_VALUE";
    private static String SIZE = "SIZE";

    private static Map<String, Integer> getListMaxValue(Iterable<IntWritable> prices) {
        Map<String, Integer> resultMap = new HashMap<>();
        int max = Integer.MIN_VALUE;
        int size = 0;
        for (IntWritable price : prices) {
            size++;
            int priceInt = price.get();
            if (max < priceInt) {
                max = priceInt;
            }
        }
        resultMap.put(MAX_VALUE, max);
        resultMap.put(SIZE, size);
        return resultMap;
    }

    public static class CountMapper extends Mapper<Object, Text, Text, IntWritable> {

        @Override
        protected void map(Object offset, Text rows, Context context) throws IOException, InterruptedException {

            String[] cols = rows.toString().split(",");
            if (cols[1].startsWith("Bud")) {
                context.write(new Text(cols[0]), new IntWritable(Integer.parseInt(cols[2])));
            }

        }

    }

    public static class CountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

        @Override
        protected void reduce(Text barName, Iterable<IntWritable> prices, Context context)
                throws IOException, InterruptedException {
            Map<String, Integer> statInfo = getListMaxValue(prices);
            if (statInfo.get(MAX_VALUE) <= 5) {
                context.write(barName, new IntWritable(statInfo.get(SIZE)));
            }
        }
    }


    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
        for (int i = 0; i < otherArgs.length; i++) {
            System.out.println(otherArgs[i]);
        }
        Job job = Job.getInstance(conf, "inf_hw5");
        job.setJarByClass(count.class);
        job.setMapperClass(CountMapper.class);
        job.setReducerClass(CountReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        for (int i = 0; i < otherArgs.length - 1; ++i) {
            FileInputFormat.addInputPath(job, new Path(otherArgs[i]));
        }
        FileOutputFormat.setOutputPath(job,
                new Path(otherArgs[otherArgs.length - 1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}

package edu.aaron.final_backend.utils;


import org.springframework.stereotype.Component;

import java.lang.reflect.Method;
import java.math.BigDecimal;
import java.text.Collator;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Locale;

public class SortList<T> {

    private Class<T> classType;

    public SortList(Class<T> classType) {
        this.classType = classType;
    }

    public List<T> getSortList(List<T> list, final String sortFiled, final String sortType) {

        Collections.sort(list, new Comparator<T>() {

            @Override
            public int compare(T o1, T o2) {
                try {
                    Method method = classType.getMethod("get" + sortFiled.substring(0, 1).toUpperCase() + sortFiled.substring(1));
                    if (method.invoke(o1) == null || method.invoke(o2) == null) {
                        return 0;
                    }
                    Collator collator = Collator.getInstance(Locale.US);
                    String result1 = method.invoke(o1).toString();
                    String result2 = method.invoke(o2).toString();
                    if (method.getReturnType().getSimpleName().equals("String")) {
                        if ("ASCE".equals(sortType.toUpperCase())) {
                            return collator.compare(result1, result2);
                        }
                        return -1 * collator.compare(result1, result2);
                    } else {
                        if ("ASCE".equals(sortType.toUpperCase())) {
                            return new BigDecimal(result1).compareTo(new BigDecimal(result2));
                        }
                        return new BigDecimal(result2).compareTo(new BigDecimal(result1));
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                }
                return 0;
            }
        });

        return list;
    }
}

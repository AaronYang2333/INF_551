package edu.aaron.final_backend.utils;

import org.springframework.stereotype.Component;

@Component
public class BoolUtil {

    public static Boolean isNull(Object obj) {
        if (null == obj) {
            return false;
        } else {
            return true;
        }
    }
}

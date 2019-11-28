package edu.aaron.final_backend.utils;

import org.springframework.stereotype.Component;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;

@Component
public class ParamsUtil {

    public static Object convertType(String field, String value) throws UnsupportedEncodingException {
        if (field.equalsIgnoreCase("\"price\"")) {
            if (null != value) {
                return Integer.parseInt(value);
            }
        } else if (field.equalsIgnoreCase("\"rate\"")) {
            if (null != value) {
                return Float.parseFloat(value);
            }
        }

        return URLEncoder.encode(value.toUpperCase(), "UTF-8");

    }

    public static Boolean isStringField(String field) {
        if (field.equalsIgnoreCase("\"flightNumber\"") ||
                field.equalsIgnoreCase("\"craftTypeCode\"") ||
                field.equalsIgnoreCase("\"priceClass\"")) {
            return Boolean.TRUE;
        }
        return Boolean.FALSE;
    }
}

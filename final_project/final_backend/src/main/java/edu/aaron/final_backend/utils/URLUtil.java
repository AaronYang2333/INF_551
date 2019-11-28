package edu.aaron.final_backend.utils;


import org.springframework.stereotype.Component;

import java.net.URLEncoder;

@Component
public class URLUtil {


    private static String BASE_URL = "https://flight-117bd.firebaseio.com/.json";

    public static String generateURL(String orderBy, String startAt, String endAt, Integer limitToFirst, Integer limitToLast) throws Exception {
        String generatedURL = BASE_URL + "?orderBy=" + URLEncoder.encode(orderBy, "UTF-8");

        if (null != startAt) {
            Object newStartAtValue = ParamsUtil.convertType(orderBy, startAt);
            generatedURL = new StringBuilder(generatedURL).append("&startAt=").append(newStartAtValue).toString();
        }
        if (null != endAt) {
            Object newEndAtValue = ParamsUtil.convertType(orderBy, endAt);
            generatedURL = new StringBuilder(generatedURL).append("&endAt=").append(newEndAtValue).toString();
        }
        if (null != limitToFirst) {
            if (ParamsUtil.isStringField(orderBy)) {
                limitToFirst += 1000;
            }
            generatedURL = new StringBuilder(generatedURL).append("&limitToFirst=").append(limitToFirst).toString();
        }
        if (null != limitToLast) {
            String prefix = "&limitToLast=";
            if (ParamsUtil.isStringField(orderBy)) {
                prefix = "&limitToFirst=";
                limitToLast += 1000;
            }
            generatedURL = new StringBuilder(generatedURL).append(prefix).append(limitToLast).toString();
        }

        return generatedURL;

    }


}

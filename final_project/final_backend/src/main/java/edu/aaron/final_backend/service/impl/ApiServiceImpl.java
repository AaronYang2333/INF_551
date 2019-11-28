package edu.aaron.final_backend.service.impl;

import com.alibaba.fastjson.JSONObject;
import com.alibaba.fastjson.TypeReference;
import edu.aaron.final_backend.entity.Ticket;
import edu.aaron.final_backend.service.ApiService;
import edu.aaron.final_backend.utils.ArrayUtil;
import edu.aaron.final_backend.utils.HttpClientUtil;
import edu.aaron.final_backend.utils.ParamsUtil;
import edu.aaron.final_backend.utils.SortList;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;

@Service
public class ApiServiceImpl implements ApiService {

    private static final Logger LOGGER = LoggerFactory.getLogger(ApiServiceImpl.class);

    @Override
    public List<Ticket> executeURL(String url) {
        String result = HttpClientUtil.doGet(url);
        LOGGER.info("execute url -> :" + url + "\"successfully!");
        if (result.startsWith("{")) {
            Map<String, Ticket> jsonObject = JSONObject.parseObject(result, new TypeReference<Map<String, Ticket>>() {
            });
            Map<String, Ticket> map = (Map<String, Ticket>) jsonObject;
            List<Ticket> list = new ArrayList<>(map.values());
            return list;
        }

        return JSONObject.parseArray(result, Ticket.class);

    }

    @Override
    public List<Ticket> sortData(List<Ticket> data, String field, Boolean isAsce) {
        int fieldNameLength = field.length();
        String orderType = "ASCE";
        if (!isAsce) {
            orderType = "DESC";
        }
        if (!field.equalsIgnoreCase("\"$key\"")) {
            List sortedList = new SortList(Ticket.class).getSortList(data, field.substring(1, fieldNameLength - 1), orderType);
            if (ParamsUtil.isStringField(field) && !isAsce) {
                ArrayUtil.reverse(sortedList);
            }
            return sortedList;
        }
        return data;
    }
}

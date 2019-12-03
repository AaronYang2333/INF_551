package edu.aaron.final_backend.controller;

import edu.aaron.final_backend.entity.Ticket;
import edu.aaron.final_backend.service.ApiService;
import edu.aaron.final_backend.utils.BoolUtil;
import edu.aaron.final_backend.utils.URLUtil;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Api(tags = "System API")
@RestController
public class ApiController {

    private static final Logger LOGGER = LoggerFactory.getLogger(ApiController.class);

    @Autowired
    private ApiService apiService;

    @CrossOrigin
    @RequestMapping(value = "/api"
            , method = RequestMethod.GET)
    @ApiOperation(value = "根据URL 获得有序数据", notes = "获得有序数据")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "orderBy", value = "要排序的列名", required = true, dataType = "string", paramType = "query"),
            @ApiImplicitParam(name = "startAt", value = "起始数值", required = false, dataType = "obj", paramType = "query"),
            @ApiImplicitParam(name = "endAt", value = "终止数值", required = false, dataType = "obj", paramType = "query"),
            @ApiImplicitParam(name = "limitToFirst", value = "要前多少行", required = false, dataType = "int", paramType = "query"),
            @ApiImplicitParam(name = "limitToLast", value = "要后多少行", required = false, dataType = "int", paramType = "query")
    })
    public List<Ticket> getAESC(String orderBy,
                                String startAt,
                                String endAt,
                                Integer limitToFirst,
                                Integer limitToLast) throws Exception {

        String url = URLUtil.generateURL(orderBy, startAt, endAt, limitToFirst, limitToLast);
        List<Ticket> data = apiService.executeURL(url);
        Boolean isAsce = BoolUtil.isNull(limitToFirst);
        return apiService.sortData(data, orderBy, isAsce);
    }


}

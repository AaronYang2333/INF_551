package edu.aaron.final_backend.entity;


import com.alibaba.fastjson.annotation.JSONField;
import lombok.Data;

import java.io.Serializable;

@Data
public class Ticket implements Serializable {
    @JSONField(name = "ID")
    private Integer ID;

    private String arrivalDate;

    private String cabinClass;
    private String craftTypeCode;

    private String createDate;
    private Integer dateDifference;

    private String departureDate;
    private String flightNumber;
    private Integer price;
    private String priceClass;
    private Float rate;
    private String traAirport;


}

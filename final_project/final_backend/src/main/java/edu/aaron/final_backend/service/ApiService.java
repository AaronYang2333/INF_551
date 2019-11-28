package edu.aaron.final_backend.service;

import edu.aaron.final_backend.entity.Ticket;

import java.util.List;
import java.util.Map;

public interface ApiService {

    List<Ticket> executeURL(String url);

    List<Ticket> sortData(List<Ticket> data, String orderBy, Boolean isAsce);
}

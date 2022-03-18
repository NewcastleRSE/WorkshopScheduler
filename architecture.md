```mermaid
graph TD;
  View-->Controller-->Model;
  View-->GUI0;
  Controller-->TKinter;
  Model-->CSV;
  
  subgraph section0
    View
    GUI0
  end
  
  subgraph section1
    Controller
    TKinter
  end  
  
  subgraph section2
    Model
    CSV
  end

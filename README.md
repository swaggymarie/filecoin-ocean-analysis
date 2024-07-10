<h1>filecoin-ocean-analysis</h1>

<h2>Global analysis </h2>
<h3>Energy performance and the evolution of Filecoin's storage </h3>
<div style='display:flex; flex-direction: row'>
     <img src="images/DataStorageCapacity_EnergyConsumption.png" width="300"/>
     <div>This graph suggests the data storage capacity always increased since filecoin launched. The energy consumption rate was following the storage capacity in the first place but stoped evolving. This means that filecoin is getting more efficient to store data! </div>
</div>


<h3>Evolution of the share of renewable energy used by Filecoin</h3>

<div style="display:flex; flex-direction:row; align-items: flex-start">
     <img src="images/totalEnergy_RenewableEnergy.png" width="200"/>
     <img style="padding-left:10px;" src="images/Share_RenewableEnergy.png" width="200"/>
</div>
<div>This shows that a huge part of the energy used is renewable (almost never under 50%), with a mean of 119.7482121194972%. The question is what is made with the energy purchased but not used ? </div>
<div>We can observe that Filecoin seams to tend to be almost 100% renewable, even though we see the ratio of renewable is increasing more slowly at the end of this period.</div>
<h2>Correlation</h2>
<h3>Between the energy used to seal the filecoin data and the price of the $FIL token </h3>
<div style='display:flex; flex-direction: row'>
     <img src="images/Price_EnergyUsedToSeal.png" width="400"/>
     <div style='display:flex; align-items: start'>
          <div>Pearson correlation (linear): 0.5836671865903877</div>
          <div>Spearman correlation (non linear): 0.7209322840753908</div>
          <div>This show a high correlation</div>
     </div>
</div>

<h3>Between the capacity of storage added per day in the Filecoin network and the price of the $FIL token </h3>
<div style='display:flex; flex-direction: row'>
     <img src="images/Price_StorageAddedPerDay.png" width="400"/>
     <div style='display:flex; align-items: start'>
          <div>Pearson correlation (linear): 0.5836671865917777</div>
          <div>Spearman correlation (non linear): 0.7209322840753908</div>
          <div>This show a high correlation</div>
     </div>
</div>

<h3>Between the energy consumption rate of the Filecoin network and the $FIL token price </h3>
<div style='display:flex; flex-direction: row'>
     <img src="images/Price_EnergyConsuptionRate.png" width="400"/>
     <div style='display:flex; align-items: start'>
          <div>Pearson correlation (linear):-0.39090893851807507</div>
          <div>Spearman correlation (non linear):-0.5233192039536365</div>
          <div>This shows a slightly negative correlation</div>
     </div>
</div>                                               
<h3>Conclusion of the correlations</h3>
The three correlations suggest that there is a positive relationship between higher price, and the energy used to seal the Filecoin data, as well as the data storage capacity added per day. This indicates that there is a high chance of augmentation of the capacity of storage added per day and energy used to seal data as we see the $FIL price increase. We would also see the energy consumption rate slightly decrease or not move, so the energy performance might be better in the future as well.

## Algorithm

## Report

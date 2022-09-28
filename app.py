# Primary Packages
import pandas as pd
import numpy as np
import streamlit as st
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import time



st.set_page_config(
    page_title="NSSC Real Time Data Dashboard",
    page_icon ="✅",
    layout="wide"
    )

st.title("Real Time Green House Data")

selection = st.selectbox("Select Green House", ["Green House I", "Green House II" ])

placeholder = st.empty()

if selection == 'Green House I':
    for seconds in range(200):
        MQTT_BROKER = "202.144.136.82"
        msg = subscribe.simple("GH1_THC", hostname=MQTT_BROKER)
        #print("%s %s" % (msg.topic, msg.payload))
        data = msg.payload
        print(data)
        dat = str(data)
        val = dat.split(",")

        tem = val[0]
        temF = tem[2:]
        hum = val[1]
        ph = val[2]
        pHF = ph[:-1]
        
        dwc = subscribe.simple("GH1_ph1", hostname=MQTT_BROKER)
        dwc_data = dwc.payload
        dwc_data_str = str(dwc_data)
        dwc_ph = dwc_data_str[2:-1]
        print(dwc_ph)

        dwc1 = subscribe.simple("GH1_EC1", hostname=MQTT_BROKER)
        dwc_data1 = dwc1.payload
        dwc_data1_str = str(dwc_data1)
        print(dwc_data1_str)
        dwc_data1_spt = dwc_data1_str.split(",")
        dwc_ec = dwc_data1_spt[0]
        dwc_tem = dwc_data1_spt[1]
        dwc_EC = dwc_ec[2:]
        dwc_TEM = dwc_tem[:-1]
        print(dwc_EC)
        print(dwc_TEM)

        dwc2 = subscribe.simple("GH1_LS", hostname=MQTT_BROKER)
        dwc_data2 = dwc2.payload
        dwc_data2_str = str(dwc_data2)
        dwc_ls = dwc_data2_str[2:-1]
        print(dwc_ls)

        nft = subscribe.simple("GH1_ph2", hostname=MQTT_BROKER)
        nft_data = nft.payload
        nft_data_str = str(nft_data)
        nft_ph = nft_data_str[2:-1]
        print(nft_ph)

        nft1 = subscribe.simple("GH1_EC2", hostname=MQTT_BROKER)
        nft_data1 = nft1.payload
        nft_data1_str = str(nft_data1)
        print(nft_data1_str)
        nft_data1_spt = nft_data1_str.split(",")
        nft_ec = nft_data1_spt[0]
        nft_tem = nft_data1_spt[1]
        nft_EC = nft_ec[2:]
        nft_TEM = nft_tem[:-1]
        print(nft_EC)
        print(nft_TEM)

        dostatus = subscribe.simple("DO_Status", hostname=MQTT_BROKER)
    #print("%s %s" % (msg.topic, msg.payload))
        status_data = dostatus.payload
        status_data_str = str(status_data)
        print(status_data_str)
        status_data_spt = status_data_str.split(",")
        deepp = status_data_spt[0]
        fdeepp = deepp[2]
        sp1 = status_data_spt[1]
        sp2 = status_data_spt[2]
        gh2 = status_data_spt[3]
        fgh2= gh2[:-1]
        print(fdeepp)
        print(sp1)
        print(sp2)
        print(fgh2)
        
        aistatus = subscribe.simple("AI_Status", hostname=MQTT_BROKER)
    #print("%s %s" % (msg.topic, msg.payload))
        status_data1 = aistatus.payload
        status_data1_str = str(status_data1)
        print(status_data1_str)
        status_data1_spt = status_data1_str.split(",")
        gh1l = status_data1_spt[0]
        fgh1l = gh1l[2]
        gh1r = status_data1_spt[1]
        gh2l = status_data1_spt[2]
        gh2r = status_data1_spt[3]
        fgh2r= gh2r[:-1]
        print(fgh1l)
        print(gh1r)
        print(gh2l)
        print(fgh2r)
    
    
        with placeholder.container():
            # create three columns
            if fgh1l == "0" and gh1r =="4095":
                st.title("Green House One is on Remote Mode")

            if fgh1l == "4095" and gh1r =="0":
                st.title("Green House One is on Local Mode ")
    



            st.title("Environment Condition")
            kpi1, kpi2, kpi3 = st.columns(3)

            # fill in those three columns with respective metrics or KPIs 
            kpi1.metric(label="Temperature", value=f"{temF} ℃")
            kpi2.metric(label="Humidity", value= f"{hum} %")
            kpi3.metric(label="Carbondioxide", value= f"{pHF}")


            st.title("Nutrient Film Technique")
            nft1, nft2, nft3 = st.columns(3)
            # fill in those three columns with respective metrics or KPIs 
            nft1.metric(label="Potential of Hydrogen", value=f"{nft_ph}")
            nft2.metric(label="Electrical Conductivity", value= f"{nft_EC} mS/cm")
            nft3.metric(label="Temperature", value= f"{nft_TEM} ℃")
            
            # create two columns for charts 
            st.title("Deep Water Culture")
            dwc1, dwc2, dwc3, dwc4 = st.columns(4)

            # fill in those three columns with respective metrics or KPIs 
            dwc1.metric(label="Potential of Hydrogen", value=f"{dwc_ph}")
            dwc2.metric(label="Electrical Conductivity", value= f"{dwc_EC} mS/cm")
            dwc3.metric(label="Temperature", value= f"{dwc_TEM} ℃")
            dwc4.metric(label="Tank Level", value= f"{dwc_ls} cm")

            if fdeepp == "0":
                st.write("Deep Water Culture Pump Off")

            if fdeepp == "1":
                st.write("Deep Water Culture Pump On")

            if sp1 == "0":
                st.write("NFT Pump One Off")

            if sp1 == "1":
                st.write("NFT Pump One On")

            if sp2 == "0":
                st.write("NFT Pump Two Off")

            if sp2 == "1":
                st.write("NFT Pump Two On")

            if fgh2 == "0":
                st.write("Drip Irrigation Pump Off")

            if fdeepp == "1":
                st.write("Deep Irrigation Pump On")
                    #st.dataframe(df)
            time.sleep(1)

if selection == 'Green House II':
    for seconds in range(200):
        MQTT_BROKER = "202.144.136.82"
        ss = subscribe.simple("GH2_SS1", hostname=MQTT_BROKER)
        ss_data = ss.payload
        ss_data_str = str(ss_data)
        ss_data_spt = ss_data_str.split(",")
        ss_hum = ss_data_spt[0]
        ss_HUM = ss_hum[2:]
                

        ss_tem = ss_data_spt[1]
        ss_con = ss_data_spt[2]
        ss_ph = ss_data_spt[3]
        ss_nitro = ss_data_spt[4]
        ss_pho = ss_data_spt[5]
        ss_pot = ss_data_spt[6]
        ss_POT = ss_pot[:-1]
        print(ss_data_str)

        gh2_ls = subscribe.simple("GH2_LS", hostname=MQTT_BROKER)
        gh2_ls_data = gh2_ls.payload
        gh2_ls_data_str = str(gh2_ls_data)
        gh2_LS = gh2_ls_data_str[2:-1]
        print(gh2_LS)

        ss2 = subscribe.simple("GH2_SS2", hostname=MQTT_BROKER)
        ss2_data = ss2.payload
        ss2_data_str = str(ss2_data)
        ss2_data_spt = ss2_data_str.split(",")
        ss2_hum = ss2_data_spt[0]
        ss2_HUM = ss2_hum[2:]
                

        ss2_tem = ss2_data_spt[1]
        ss2_con = ss2_data_spt[2]
        ss2_ph = ss2_data_spt[3]
        ss2_nitro = ss2_data_spt[4]
        ss2_pho = ss2_data_spt[5]
        ss2_pot = ss2_data_spt[6]
        ss2_POT = ss2_pot[:-1]
        print(ss2_data_str)

        aistatus = subscribe.simple("AI_Status", hostname="192.168.124.72")
    #print("%s %s" % (msg.topic, msg.payload))
        status_data1 = aistatus.payload
        status_data1_str = str(status_data1)
        print(status_data1_str)
        status_data1_spt = status_data1_str.split(",")
        gh1l = status_data1_spt[0]
        fgh1l = gh1l[2]
        gh1r = status_data1_spt[1]
        gh2l = status_data1_spt[2]
        gh2r = status_data1_spt[3]
        fgh2r= gh2r[:-1]
        print(fgh1l)
        print(gh1r)
        print(gh2l)
        print(fgh2r)

        with placeholder.container():
            # create three columns
            if gh2l == "0" and fgh2r =="4095":
                st.title("Green House Two is on Remote Mode")

            else:
                st.title("Green House Two is on Local Mode ")

            st.title("Drip Irrigation Row One")
            drpOne1, drpOne2, drpOne3, drpOne4 = st.columns(4)

            # fill in those three columns with respective metrics or KPIs 
            drpOne1.metric(label="Humidity", value=f"{ss_HUM} %")
            drpOne2.metric(label="Temperature", value= f"{ss_tem} ℃")
            drpOne3.metric(label="Conductivity", value= f"{ss_con} mS/cm")
            drpOne4.metric(label="Potential of Hydrogen", value= f"{ss_ph}")

            drpOne5, drpOne6, drpOne7, drpOne8 = st.columns(4)
            drpOne5.metric(label="Nitrogen", value=f"{ss_nitro} ")
            drpOne6.metric(label="Phosphorus", value= f"{ss_pho} ")
            drpOne7.metric(label="Potassium", value= f"{ss_pot} ")
            drpOne8.metric(label="Tank Level", value= f"{gh2_LS}")

            # create two columns for charts 
            st.title("Drip Irrigation Row Two")
            
            drpTwo1, drpTwo2, drpTwo3, drpTwo4 = st.columns(4)

            # fill in those three columns with respective metrics or KPIs 
            drpTwo1.metric(label="Humidity", value=f"{ss2_HUM} %")
            drpTwo2.metric(label="Temperature", value= f"{ss2_tem} ℃")
            drpTwo3.metric(label="Conductivity", value= f"{ss2_con} mS/cm")
            drpTwo4.metric(label="Potential of Hydrogen", value= f"{ss2_ph}")

            drpTwo5, drpTwo6, drpTwo7, drpTwo8 = st.columns(4)
            drpTwo5.metric(label="Nitrogen", value=f"{ss2_nitro} ")
            drpTwo6.metric(label="Phosphorus", value= f"{ss2_pho} ")
            drpTwo7.metric(label="Potassium", value= f"{ss2_pot} ")
            drpTwo8.metric(label="Tank Level", value= f"{gh2_LS}")
            #st.dataframe(df)
            time.sleep(1)

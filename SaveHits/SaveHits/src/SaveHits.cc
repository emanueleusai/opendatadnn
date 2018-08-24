// -*- C++ -*-
//
// Package:    SaveHits
// Class:      SaveHits
// 
/**\class SaveHits SaveHits.cc SaveHits/SaveHits/src/SaveHits.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Emanuele Usai,,,
//         Created:  Tue Aug 21 07:28:17 CEST 2018
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

//added
#include <string>
#include <iostream>
#include <vector>

#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHitCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripMatchedRecHit2DCollection.h"
#include "DataFormats/TrackerRecHit2D/interface/SiStripRecHit2DCollection.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"

//#include "Geometry/CommonDetUnit/interface/TrackingGeometry.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/CommonDetUnit/interface/GeomDetType.h"
#include "Geometry/CommonDetUnit/interface/GeomDetUnit.h"

#include "Geometry/TrackerGeometryBuilder/interface/PixelGeomDetUnit.h"
#include "Geometry/TrackerGeometryBuilder/interface/PixelGeomDetType.h"
#include "Geometry/TrackerGeometryBuilder/interface/StripGeomDetUnit.h"
#include "Geometry/TrackerGeometryBuilder/interface/StripGeomDetType.h"

#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/CommonTopologies/interface/PixelTopology.h"
#include "Geometry/CommonTopologies/interface/StripTopology.h"

#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/SiPixelDetId/interface/PXBDetId.h"
#include "DataFormats/SiPixelDetId/interface/PXFDetId.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"
#include "DataFormats/SiStripDetId/interface/TECDetId.h"
#include "DataFormats/SiStripDetId/interface/TIBDetId.h"
#include "DataFormats/SiStripDetId/interface/TIDDetId.h"
#include "DataFormats/SiStripDetId/interface/TOBDetId.h"
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h"

// To use root histos
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "TrackingTools/PatternTools/interface/Trajectory.h"

#include "TTree.h"

#include "DataFormats/TrackingRecHit/interface/TrackingRecHitFwd.h"

//
// class declaration
//

class SaveHits : public edm::EDAnalyzer {
   public:
      explicit SaveHits(const edm::ParameterSet&);
      ~SaveHits();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------
      TFile * tf1;
      TTree * hits_tree;
      TTree * tracks_tree;

      std::vector<Float_t> hit_global_x;
      std::vector<Float_t> hit_global_y;
      std::vector<Float_t> hit_global_z;
      std::vector<Float_t> hit_local_x;
      std::vector<Float_t> hit_local_y;
      std::vector<Float_t> hit_local_x_error;
      std::vector<Float_t> hit_local_y_error;
      // std::vector<Float_t> hit_cluster_global_x;
      // std::vector<Float_t> hit_cluster_global_y;
      // std::vector<Float_t> hit_cluster_global_z;
      // std::vector<Float_t> hit_cluster_local_x;
      // std::vector<Float_t> hit_cluster_local_y;
      // std::vector<Float_t> hit_cluster_local_x_error;
      // std::vector<Float_t> hit_cluster_local_y_error;
      // std::vector<Float_t> hit_cluster_charge;
      // std::vector<UInt_t>  hit_cluster_size;
      // std::vector<UInt_t>  hit_cluster_size_x;
      // std::vector<UInt_t>  hit_cluster_size_y;
      std::vector<UInt_t>  hit_sub_det; //1 PixelBarrel, 2 PixelEndcap, 3 TIB, 4 TOB, 5 TID, 6 TEC
      std::vector<UInt_t>  hit_layer;


      std::vector<Float_t> track_chi2;
      std::vector<Float_t> track_ndof;
      std::vector<Float_t> track_chi2ndof;
      std::vector<Float_t> track_charge;
      std::vector<Float_t> track_momentum;
      std::vector<Float_t> track_pt;
      std::vector<Float_t> track_pterr;
      std::vector<UInt_t>  track_hitsvalid;
      std::vector<UInt_t>  track_hitslost;
      std::vector<Float_t> track_theta;
      std::vector<Float_t> track_thetaerr;
      std::vector<Float_t> track_phi;
      std::vector<Float_t> track_phierr;
      std::vector<Float_t> track_eta;
      std::vector<Float_t> track_etaerr;
      std::vector<Float_t> track_dxy;
      std::vector<Float_t> track_dxyerr;
      std::vector<Float_t> track_dsz;
      std::vector<Float_t> track_dszerr;
      std::vector<Float_t> track_qoverp;
      std::vector<Float_t> track_qoverperr;
      std::vector<Float_t> track_vx;
      std::vector<Float_t> track_vy;
      std::vector<Float_t> track_vz;
      std::vector<Int_t>   track_algo;
      std::vector<std::vector<Float_t> > track_hit_global_x;
      std::vector<std::vector<Float_t> > track_hit_global_y;
      std::vector<std::vector<Float_t> > track_hit_global_z;
      std::vector<std::vector<Float_t> > track_hit_local_x;
      std::vector<std::vector<Float_t> > track_hit_local_y;
      std::vector<std::vector<Float_t> > track_hit_local_x_error;
      std::vector<std::vector<Float_t> > track_hit_local_y_error;
      std::vector<std::vector<UInt_t> >  track_hit_sub_det; //1 PixelBarrel, 2 PixelEndcap, 3 TIB, 4 TOB, 5 TID, 6 TEC
      std::vector<std::vector<UInt_t> >  track_hit_layer;

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
SaveHits::SaveHits(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed

   tf1         = new TFile("savehits_output.root", "RECREATE");  
   hits_tree   = new TTree("hits_tree","hits_tree");
   tracks_tree = new TTree("tracks_tree","tracks_tree");

   hits_tree->Branch("hit_global_x",&hit_global_x);
   hits_tree->Branch("hit_global_y",&hit_global_y);
   hits_tree->Branch("hit_global_z",&hit_global_z);
   hits_tree->Branch("hit_local_x",&hit_local_x);
   hits_tree->Branch("hit_local_y",&hit_local_y);
   hits_tree->Branch("hit_local_x_error",&hit_local_x_error);
   hits_tree->Branch("hit_local_y_error",&hit_local_y_error);
   // hits_tree->Branch("hit_cluster_global_x",&hit_cluster_global_x);
   // hits_tree->Branch("hit_cluster_global_y",&hit_cluster_global_y);
   // hits_tree->Branch("hit_cluster_global_z",&hit_cluster_global_z);
   // hits_tree->Branch("hit_cluster_local_x",&hit_cluster_local_x);
   // hits_tree->Branch("hit_cluster_local_y",&hit_cluster_local_y);
   // hits_tree->Branch("hit_cluster_local_x_error",&hit_cluster_local_x_error);
   // hits_tree->Branch("hit_cluster_local_y_error",&hit_cluster_local_y_error);
   // hits_tree->Branch("hit_cluster_charge",&hit_cluster_charge);
   // hits_tree->Branch("hit_cluster_size",&hit_cluster_size);
   // hits_tree->Branch("hit_cluster_size_x",&hit_cluster_size_x);
   // hits_tree->Branch("hit_cluster_size_y",&hit_cluster_size_y);
   hits_tree->Branch("hit_sub_det",&hit_sub_det);
   hits_tree->Branch("hit_layer",&hit_layer);


   tracks_tree->Branch("track_chi2",&track_chi2);
   tracks_tree->Branch("track_ndof",&track_ndof);
   tracks_tree->Branch("track_chi2ndof",&track_chi2ndof);
   tracks_tree->Branch("track_charge",&track_charge);
   tracks_tree->Branch("track_momentum",&track_momentum);
   tracks_tree->Branch("track_pt",&track_pt);
   tracks_tree->Branch("track_pterr",&track_pterr);
   tracks_tree->Branch("track_hitsvalid",&track_hitsvalid);
   tracks_tree->Branch("track_hitslost",&track_hitslost);
   tracks_tree->Branch("track_theta",&track_theta);
   tracks_tree->Branch("track_thetaerr",&track_thetaerr);
   tracks_tree->Branch("track_phi",&track_phi);
   tracks_tree->Branch("track_phierr",&track_phierr);
   tracks_tree->Branch("track_eta",&track_eta);
   tracks_tree->Branch("track_etaerr",&track_etaerr);
   tracks_tree->Branch("track_dxy",&track_dxy);
   tracks_tree->Branch("track_dxyerr",&track_dxyerr);
   tracks_tree->Branch("track_dsz",&track_dsz);
   tracks_tree->Branch("track_dszerr",&track_dszerr);
   tracks_tree->Branch("track_qoverp",&track_qoverp);
   tracks_tree->Branch("track_qoverperr",&track_qoverperr);
   tracks_tree->Branch("track_vx",&track_vx);
   tracks_tree->Branch("track_vy",&track_vy);
   tracks_tree->Branch("track_vz",&track_vz);
   tracks_tree->Branch("track_algo",&track_algo);


}


SaveHits::~SaveHits()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)
  tf1->cd();
  hits_tree->Write();
  tracks_tree->Write();
  tf1->Write();
  tf1->Close(); 
}


//
// member functions
//

// ------------ method called for each event  ------------
void
SaveHits::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  hit_global_x.clear();
  hit_global_y.clear();
  hit_global_z.clear();
  hit_local_x.clear();
  hit_local_y.clear();
  hit_local_x_error.clear();
  hit_local_y_error.clear();
  // hit_cluster_global_x.clear();
  // hit_cluster_global_y.clear();
  // hit_cluster_global_z.clear();
  // hit_cluster_local_x.clear();
  // hit_cluster_local_y.clear();
  // hit_cluster_local_x_error.clear();
  // hit_cluster_local_y_error.clear();
  // hit_cluster_charge.clear();
  // hit_cluster_size.clear();
  // hit_cluster_size_x.clear();
  // hit_cluster_size_y.clear();
  hit_sub_det.clear();
  hit_layer.clear();


  track_chi2.clear();
  track_ndof.clear();
  track_chi2ndof.clear();
  track_charge.clear();
  track_momentum.clear();
  track_pt.clear();
  track_pterr.clear();
  track_hitsvalid.clear();
  track_hitslost.clear();
  track_theta.clear();
  track_thetaerr.clear();
  track_phi.clear();
  track_phierr.clear();
  track_eta.clear();
  track_etaerr.clear();
  track_dxy.clear();
  track_dxyerr.clear();
  track_dsz.clear();
  track_dszerr.clear();
  track_qoverp.clear();
  track_qoverperr.clear();
  track_vx.clear();
  track_vy.clear();
  track_vz.clear();
  track_algo.clear();

  edm::ESHandle<TrackerGeometry> geom;
  iSetup.get<TrackerDigiGeometryRecord>().get( geom );
  const TrackerGeometry& theTracker(*geom);


//sipixel
  edm::Handle<SiPixelRecHitCollection> recHitColl;
  iEvent.getByLabel( edm::InputTag("siPixelRecHits") , recHitColl);

  SiPixelRecHitCollection::const_iterator recHitIdIterator      = (recHitColl.product())->begin();
  SiPixelRecHitCollection::const_iterator recHitIdIteratorEnd   = (recHitColl.product())->end();

  for ( ; recHitIdIterator != recHitIdIteratorEnd; recHitIdIterator++)
  {
    SiPixelRecHitCollection::DetSet detset = *recHitIdIterator;
    DetId detId = DetId(detset.detId()); // Get the Detid object
    //unsigned int detType=detId.det();    // det type, tracker=1
    unsigned int subid=detId.subdetId(); //subdetector type, barrel=1, fpix=2
    unsigned int layer = 100;

    if(subid==1)
    {  // Subdet it, pix barrel=1 
      
      PXBDetId pdetId = PXBDetId(detId);
      // unsigned int detTypeP=pdetId.det();
      // unsigned int subidP=pdetId.subdetId();
      // Barell layer = 1,2,3
      layer=pdetId.layer();
    }  
    else
    {
      PXFDetId pdetId = PXFDetId(detId.rawId());
      layer=pdetId.disk(); //1,2,3
    } // end BPix FPix if

    const PixelGeomDetUnit * theGeomDet = dynamic_cast<const PixelGeomDetUnit*> (theTracker.idToDet(detId) );

    SiPixelRecHitCollection::DetSet::const_iterator pixeliter=detset.begin();
    SiPixelRecHitCollection::DetSet::const_iterator rechitRangeIteratorEnd   = detset.end();
    for(;pixeliter!=rechitRangeIteratorEnd;++pixeliter)
    {//loop on the rechit


      LocalPoint lp = pixeliter->localPosition();
      LocalError le = pixeliter->localPositionError();
      // float xRecHit = lp.x();
      // float yRecHit = lp.y();

      // MeasurementPoint mp = topol->measurementPosition(xRecHit,yRecHit);
      GlobalPoint GP = theGeomDet->surface().toGlobal(Local3DPoint(lp));
      //theGeomDet->toGlobal(lp).x()
      //theStripDet->toGlobal(hit.localPosition()).x();
      //dynamic_cast<const StripGeomDetUnit*>( theTrackerGeometry->idToDet( hit.geographicalId() ) );
      //std::cout<<"["<<GP.x()<<", "<<GP.y()<<", "<<GP.z()<<"],"<<std::endl;
      //edm::Ref<edmNew::DetSetVector<SiPixelCluster>, SiPixelCluster> const& clust = pixeliter->cluster();

      //std::cout<<"["<<lp.x()<<", "<<clust->x()<<", "<<lp.y()<<"],"<<clust->y()<<std::endl;
      if (pixeliter->isValid())
      {
        hit_sub_det.push_back(subid);
        hit_layer.push_back(layer);
        hit_global_x.push_back(GP.x());
        hit_global_y.push_back(GP.y());
        hit_global_z.push_back(GP.z());
        hit_local_x.push_back(lp.x());
        hit_local_y.push_back(lp.y());
        hit_local_x_error.push_back(sqrt(le.xx()));
        hit_local_y_error.push_back(sqrt(le.yy()));
      }
      // hit_cluster_global_x.push_back();
      // hit_cluster_global_y.push_back();
      // hit_cluster_global_z.push_back();
      // hit_cluster_local_x.push_back(clust->x());
      // hit_cluster_local_y.push_back(clust->y());
      // hit_cluster_local_x_error.push_back(0);
      // hit_cluster_local_y_error.push_back(0);
      // hit_cluster_charge.push_back((clust->charge())/1000.);
      // hit_cluster_size.push_back(clust->size());
      // hit_cluster_size_x.push_back(clust->sizeX());
      // hit_cluster_size_y.push_back(clust->sizeY());
      


    } //rechits
  } //detid

//sistrip
  std::vector<std::string> collections;
  collections.push_back("rphiRecHit");
  collections.push_back("stereoRecHit");

for (unsigned int the_collection=0; the_collection<collections.size();the_collection++){
  edm::Handle<SiStripRecHit2DCollection> stripRecHitColl;
  iEvent.getByLabel( edm::InputTag("siStripMatchedRecHits",collections[the_collection]) , stripRecHitColl);

  SiStripRecHit2DCollection::const_iterator stripRecHitIdIterator      = (stripRecHitColl.product())->begin();
  SiStripRecHit2DCollection::const_iterator stripRecHitIdIteratorEnd   = (stripRecHitColl.product())->end();

  for (; stripRecHitIdIterator != stripRecHitIdIteratorEnd; ++stripRecHitIdIterator)
  { 
     SiStripRecHit2DCollection::DetSet detset = *stripRecHitIdIterator;
     DetId detId = DetId(detset.detId()); // Get the Detid object
     //unsigned int detType=detId.det();    // det type, tracker=1
     unsigned int subid=detId.subdetId(); //subdetector type, barrel=1, fpix=2
     unsigned int layer = 100;

     switch(subid)
     {
      case 3://TIB
      {
        TIBDetId pdetId = TIBDetId(detId);
        layer=pdetId.layer();
      }
      break;

      case 4://TID
      {
        TIDDetId pdetId = TIDDetId(detId);
        layer=pdetId.wheel();
      }
      break;

      case 5://TOB
      {
        TOBDetId pdetId = TOBDetId(detId);
        layer=pdetId.layer();
      }
      break;

      case 6://TEC
      {
        TECDetId pdetId = TECDetId(detId);
        layer=pdetId.wheel();
      }
      break;
     }
    //std::cout<<layer;
     //const StripGeomDetUnit * theGeomDet = dynamic_cast<const StripGeomDetUnit*> (theTracker.idToDet(detId) );

     SiStripRecHit2DCollection::DetSet::const_iterator stripiter=detset.begin();
     SiStripRecHit2DCollection::DetSet::const_iterator stripRechitRangeIteratorEnd   = detset.end();

     for(;stripiter!=stripRechitRangeIteratorEnd;++stripiter)
     //for(SiStripMatchedRecHit2DCollection::DetSet::const_iterator iter=detunit_iterator->begin(), end = detunit_iterator->end(); iter != end; ++iter)
     {
      const StripGeomDetUnit* theGeomDet = dynamic_cast<const StripGeomDetUnit*>( theTracker.idToDet( stripiter->geographicalId() ) );
      LocalPoint lp = stripiter->localPosition();
      LocalError le = stripiter->localPositionError();
      //std::cout<<lp.x()<<std::endl;
      GlobalPoint GP = theGeomDet->surface().toGlobal(Local3DPoint(lp));
      //std::cout<<theGeomDet->toGlobal(lp).x();
      // //theStripDet->toGlobal(hit.localPosition()).x();
      // //dynamic_cast<const StripGeomDetUnit*>( theTrackerGeometry->idToDet( hit.geographicalId() ) );
      // //std::cout<<"["<<GP.x()<<", "<<GP.y()<<", "<<GP.z()<<"],"<<std::endl;
      // //edm::Ref<edmNew::DetSetVector<SiPixelCluster>, SiPixelCluster> const& clust = pixeliter->cluster();
      //std::cout<<lp.x()<<std::endl;
      if (stripiter->isValid())
      {
       //   std::cout<<lp.x()<<std::endl;
      hit_sub_det.push_back(subid);
      hit_layer.push_back(layer);
      hit_global_x.push_back(GP.x());
      hit_global_y.push_back(GP.y());
      hit_global_z.push_back(GP.z());
      hit_local_x.push_back(lp.x());
      hit_local_y.push_back(lp.y());
      hit_local_x_error.push_back(sqrt(le.xx()));
      hit_local_y_error.push_back(sqrt(le.yy()));}
     }
  }
}
//tracks
  edm::Handle<std::vector<reco::Track> > trackColl;
  iEvent.getByLabel( edm::InputTag("generalTracks") , trackColl);
  std::vector<reco::Track>::const_iterator trackIterator      = (trackColl.product())->begin();
  std::vector<reco::Track>::const_iterator trackIteratorEnd   = (trackColl.product())->end();

  for ( ; trackIterator != trackIteratorEnd; trackIterator++)
  {

    track_chi2.push_back(      trackIterator->chi2());
    track_ndof.push_back(      trackIterator->ndof());
    track_chi2ndof.push_back(  trackIterator->chi2()/trackIterator->ndof());
    track_charge.push_back(    trackIterator->charge());
    track_momentum.push_back(  trackIterator->p());
    track_pt.push_back(        trackIterator->pt());
    track_pterr.push_back(     trackIterator->ptError());
    track_hitsvalid.push_back( trackIterator->numberOfValidHits());
    track_hitslost.push_back(  trackIterator->numberOfLostHits());
    track_theta.push_back(     trackIterator->theta());
    track_thetaerr.push_back(  trackIterator->thetaError());
    track_phi.push_back(       trackIterator->phi());
    track_phierr.push_back(    trackIterator->phiError());
    track_eta.push_back(       trackIterator->eta());
    track_etaerr.push_back(    trackIterator->etaError());
    track_dxy.push_back(       trackIterator->dxy());
    track_dxyerr.push_back(    trackIterator->dxyError());
    track_dsz.push_back(       trackIterator->dsz());
    track_dszerr.push_back(    trackIterator->dszError());
    track_qoverp.push_back(    trackIterator->qoverp());
    track_qoverperr.push_back( trackIterator->qoverpError());
    track_vx.push_back(        trackIterator->vx());
    track_vy.push_back(        trackIterator->vy());
    track_vz.push_back(        trackIterator->vz());
    track_algo.push_back(      (Int_t) trackIterator->algo());

    trackingRecHit_iterator rechit_it = trackIterator->recHitsBegin();
    trackingRecHit_iterator rechit_end = trackIterator->recHitsEnd();
    for (;rechit_it!=rechit_end;rechit_it++)
    {
      if ((*rechit_it)->isValid())
      {
        DetId the_detid = (*rechit_it)->geographicalId();
        if (the_detid.det()!=1) continue; //only tracker
        if (the_detid.subdetId()==1 || the_detid.subdetId()==2)
        {
          const PixelGeomDetUnit* theGeomDet = dynamic_cast<const PixelGeomDetUnit*>( theTracker.idToDet( (*rechit_it)->geographicalId() ) );
          LocalPoint lp = (*rechit_it)->localPosition();
          GlobalPoint GP = theGeomDet->surface().toGlobal(Local3DPoint(lp));
          //std::cout<<GP.x()<<std::endl;
        }
        if (the_detid.subdetId()>=3 && the_detid.subdetId()<=6)
        {
          const StripGeomDetUnit* theGeomDet = dynamic_cast<const StripGeomDetUnit*>( theTracker.idToDet( (*rechit_it)->geographicalId() ) );
          LocalPoint lp = (*rechit_it)->localPosition();
          GlobalPoint GP = theGeomDet->surface().toGlobal(Local3DPoint(lp));
          std::cout<<GP.x()<<std::endl;
        }
        //std::cout<<(*rechit_it)->localPosition().x()<<std::endl;


std::vector<std::vector<Float_t> > track_hit_global_x;
      std::vector<std::vector<Float_t> > track_hit_global_y;
      std::vector<std::vector<Float_t> > track_hit_global_z;
      std::vector<std::vector<Float_t> > track_hit_local_x;
      std::vector<std::vector<Float_t> > track_hit_local_y;
      std::vector<std::vector<Float_t> > track_hit_local_x_error;
      std::vector<std::vector<Float_t> > track_hit_local_y_error;
      std::vector<std::vector<UInt_t> >  track_hit_sub_det; //1 PixelBarrel, 2 PixelEndcap, 3 TIB, 4 TOB, 5 TID, 6 TEC
      std::vector<std::vector<UInt_t> >  track_hit_layer;

  //        id_type rawId() const { return m_id;}
  // DetId geographicalId() const {return m_id;}
  
  // virtual LocalPoint localPosition() const = 0;
  
  // virtual LocalError localPositionError() const = 0;
      }
      

    }

  }

  hits_tree->Fill();
  tracks_tree->Fill();
}


// ------------ method called once each job just before starting event loop  ------------
void 
SaveHits::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SaveHits::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
void 
SaveHits::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
SaveHits::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
SaveHits::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
SaveHits::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SaveHits::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SaveHits);

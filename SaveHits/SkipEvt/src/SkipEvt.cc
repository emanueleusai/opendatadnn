// -*- C++ -*-
//
// Package:    SkipEvt
// Class:      SkipEvt
// 
/**\class SkipEvt SkipEvt.cc SaveHits/SkipEvt/src/SkipEvt.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Emanuele Usai,,,
//         Created:  Tue Jan 15 18:43:55 CET 2019
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

//
// class declaration
//

class SkipEvt : public edm::EDFilter {
   public:
      explicit SkipEvt(const edm::ParameterSet&);
      ~SkipEvt();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
   	  unsigned long event_count;
   	  unsigned long first_event;
   	  unsigned long last_event;
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      virtual bool beginRun(edm::Run&, edm::EventSetup const&);
      virtual bool endRun(edm::Run&, edm::EventSetup const&);
      virtual bool beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      virtual bool endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      // ----------member data ---------------------------
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
SkipEvt::SkipEvt(const edm::ParameterSet& iConfig)
{
   //now do what ever initialization is needed
	first_event  = iConfig.getParameter<int>("first_event");
	last_event  = iConfig.getParameter<int>("last_event");
	event_count=0;

}


SkipEvt::~SkipEvt()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
SkipEvt::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   event_count = event_count + 1;
   std::cout<<std::endl<<((event_count-1)>=first_event && (event_count-1)<=last_event)<<std::endl;
   return ((event_count-1)>=first_event && (event_count-1)<=last_event);
}

// ------------ method called once each job just before starting event loop  ------------
void 
SkipEvt::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SkipEvt::endJob() {
}

// ------------ method called when starting to processes a run  ------------
bool 
SkipEvt::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool 
SkipEvt::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool 
SkipEvt::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool 
SkipEvt::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SkipEvt::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(SkipEvt);

#ifndef _MOVE_MODEL_HH_
#define _MOVE_MODEL_HH_

#include <vector>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>

using namespace gazebo;

namespace gazebo
{
    class ModelMove : public ModelPlugin
  {
      public: VelodynePlugin() {}

      public: virtual void Load(physics::ModelPtr _model, sdf::ElementPtr _sdf)
    {
      // Just output a message for now
      std::cerr << "\n Model: " <<
        _model->GetName() << " ["<<
        _sdf->GetName() << " [";
    }
  };

  GZ_REGISTER_MODEL_PLUGIN(ModelMove)
}
#endif
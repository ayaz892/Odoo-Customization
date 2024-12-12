#Click on the Post Button in PO will call this function and will Automatically post the quantity/receipt and JV in PO.

    def button_post_jv_and_receipt(self):
        if self.entry_id and self.entry_id.state == 'draft':
            self.entry_id.action_post()

        for picking in self.picking_ids:
            if picking.state not in ('done', 'cancel'):
                if picking.state == 'draft':
                    picking.action_confirm()
                if picking.state in ('waiting', 'confirmed'):
                    picking.action_assign()
                if picking.state == 'assigned':
                    for move in picking.move_lines:
                        if move.quantity_done == 0:
                            move.quantity_done = move.product_uom_qty
                    picking.button_validate()

# In the xml file just add the button in PO Form Header and assign this action.
